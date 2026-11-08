from inventory.store import Store


def summary(store: Store):
    lines = []
    for name in sorted(store.items):
        lines.append(f"{name}: {store.get_count(name)}")
    return "\n".join(lines)
