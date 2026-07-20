class YAMLError(Exception):
    pass


def _strip_comment(value):
    quote = None
    for index, char in enumerate(value):
        if char in ("'", '"'):
            quote = None if quote == char else char if quote is None else quote
        if char == "#" and quote is None:
            return value[:index].rstrip()
    return value


def _scalar(value):
    value = _strip_comment(value.strip())
    if not value:
        return {}
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value in ("true", "false"):
        return value == "true"
    if value in ("null", "~"):
        return None
    try:
        return int(value)
    except ValueError:
        return value


def safe_load(text):
    if hasattr(text, "read"):
        text = text.read()
    if text is None:
        return None

    root = {}
    stack = [(-1, root)]

    for raw_line in str(text).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.strip() in ("---", "..."):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if line.startswith("- "):
            raise YAMLError("list syntax is not supported by Fabricator yaml shim")
        if ":" not in line:
            raise YAMLError(f"unsupported YAML line: {raw_line!r}")

        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise YAMLError(f"invalid indentation: {raw_line!r}")

        key, value = line.split(":", 1)
        key = key.strip()
        if not key:
            raise YAMLError("empty key")

        parent = stack[-1][1]
        parsed = _scalar(value)
        parent[key] = parsed
        if isinstance(parsed, dict):
            stack.append((indent, parsed))

    return root
