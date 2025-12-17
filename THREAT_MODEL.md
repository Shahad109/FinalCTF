# FinalCTF Threat Model

## Assets
- Target web application endpoints
- User-supplied URLs
- Local system executing the tool

## Threats
- Misuse against unauthorized systems
- False positives due to simple payload checks
- Network interception (MITM)

## Assumptions
- Tool is used only in authorized lab environments
- Targets are intentionally vulnerable (DVWA, Juice Shop)
- User understands ethical hacking constraints

## Mitigations
- Non-destructive payloads only
- No privilege escalation or persistence
- Ethical-use disclaimer in README
