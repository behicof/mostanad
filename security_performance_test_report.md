# گزارش تست امنیت و عملکرد سیستم لاگین
**تاریخ:** 2025-05-13 00:16:11 UTC
**تستر:** behicof
**محیط تست:** Production-like

## 1. تست‌های امنیتی (Security Tests)

### 1.1 تست هش رمز عبور
```python
password_hash_tests = {
    "algorithm": "bcrypt",
    "rounds": 12,
    "test_cases": [
        {
            "password": "Test@123",
            "expected_time": "< 300ms",
            "memory_usage": "< 100MB"
        },
        {
            "password": "LongP@ssw0rd123!",
            "expected_time": "< 300ms",
            "memory_usage": "< 100MB"
        }
    ]
}

def test_password_hashing():
    from passlib.hash import bcrypt
    
    results = []
    for case in password_hash_tests["test_cases"]:
        start_time = time.time()
        hashed = bcrypt.hash(case["password"])
        verification = bcrypt.verify(case["password"], hashed)
        execution_time = (time.time() - start_time) * 1000
        
        results.append({
            "execution_time": execution_time,
            "verification": verification,
            "hash_length": len(hashed)
        })