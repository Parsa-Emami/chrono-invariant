from collections import Counter
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def instants(values, zone):
    counts = Counter()
    for raw in values:
        local = datetime.fromisoformat(raw)
        if local.utcoffset() is None:
            raise ValueError("explicit UTC offsets are required")
        in_zone = local.astimezone(zone)
        if local.utcoffset() != in_zone.utcoffset():
            raise ValueError("timestamp offset disagrees with the declared time zone")
        counts[local.astimezone(timezone.utc).isoformat()] += 1
    return counts


def evaluate(data, fixture_path):
    zone = ZoneInfo(data["zone"])
    expected = instants(data["expected"], zone)
    observed = instants(data["observed"], zone)
    if any(count > 1 for count in expected.values()):
        raise ValueError("expected instants must be unique")
    findings = []
    for instant in sorted(expected.keys() | observed.keys()):
        count = observed[instant]
        if expected[instant] and count == 0:
            findings.append({"code": "missing_execution", "instant": instant})
        if not expected[instant] and count > 0:
            findings.append({"code": "unexpected_execution", "instant": instant})
        if count > 1:
            findings.append({"code": "duplicate_execution", "instant": instant, "count": count})
    return findings
