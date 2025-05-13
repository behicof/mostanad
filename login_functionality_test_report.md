# گزارش جامع تست عملکرد لاگین
**تاریخ:** 2025-05-13 01:16:44 UTC
**تستر:** behicof
**محیط:** Production-grade test environment

## 1. نتایج اجرای تست

### 1.1 نتایج تفصیلی سناریوها
```python
test_results = {
    "TC-LOGIN-01": {
        "scenario": "Valid login credentials",
        "input": {
            "username": "valid_user",
            "password": "valid_pwd"
        },
        "actual_result": "Successfully logged in, redirected to /dashboard",
        "status": "PASS",
        "response_time": "120ms"
    },
    "TC-LOGIN-02": {
        "scenario": "Invalid password",
        "input": {
            "username": "valid_user",
            "password": "wrong_pwd"
        },
        "actual_result": "Error: Invalid credentials displayed",
        "status": "PASS",
        "response_time": "115ms"
    },
    "TC-LOGIN-03": {
        "scenario": "Non-existent username",
        "input": {
            "username": "no_user",
            "password": "any_pwd"
        },
        "actual_result": "Error: Invalid credentials displayed",
        "status": "PASS",
        "response_time": "118ms"
    },
    "TC-LOGIN-04": {
        "scenario": "Blank fields",
        "input": {
            "username": "",
            "password": ""
        },
        "actual_result": "Error: Required fields cannot be empty",
        "status": "PASS",
        "response_time": "65ms"
    },
    "TC-LOGIN-05": {
        "scenario": "SQL injection attempt",
        "input": {
            "username": "' OR 1=1 --",
            "password": "any_pwd"
        },
        "actual_result": "Request blocked by WAF",
        "status": "PASS",
        "response_time": "95ms"
    }
}