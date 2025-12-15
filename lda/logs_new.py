from lda.commands import ActionableKeywords

def classify_log(logs):
    actionable = []
    ignored = {'Non_actionable':[], 'Not_matched':[]}
    
    for log in logs:
        if any(k in log for k in ActionableKeywords.NON_ACTIONABLE_KEYWORDS):
            ignored['Non_actionable'].append(log)
            continue
        
        matched = False
        
        for issue_type, patterns in ActionableKeywords.ACTIONABLE_PATTERNS.items():
            if any(p in log for p in patterns):
                actionable.append({
                    "type":issue_type,
                    "log": log
                })
                
                matched = True
                break
        if not matched:
            ignored['Not_matched'].append(log)
    return actionable, ignored

def extract_actionable_issues(actionable_logs):
    issues = []
    for item in actionable_logs:
        if item["type"] == "permission":
            issues.append({
                "error":"Permission issue",
                "details": item["log"],
                "suggested_action": "Check file ownership and permissions"
            })
        elif item["type"] == "dns":
            issues.append({
                "error": "DNS resolution failed",
                "details": item["log"],
                "suggested_action": "Check /etc/resolv.conf or systemd-resolved"
            })
        elif item["type"] == "service":
            issues.append({
                "error": "Service failed",
                "details": item["log"],
                "suggested_action": "Check systemctl status <service>"
            })
            
    return issues