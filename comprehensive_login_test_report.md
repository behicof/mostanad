# گزارش جامع تست سیستم لاگین
**تاریخ:** 2025-05-13 00:18:02
**تستر:** behicof
**نوع تست:** امنیتی و عملکردی

## 1. تست‌های امنیتی

### 1.1 تست هش رمز عبور (bcrypt)
```python
test_results = {
    "algorithm": "bcrypt",
    "rounds": 12,
    "tests_executed": [
        {
            "type": "hash_generation",
            "samples": 1000,
            "avg_time": 245,  # milliseconds
            "memory_usage": "85MB",
            "status": "PASS"
        },
        {
            "type": "verification",
            "samples": 1000,
            "avg_time": 242,  # milliseconds
            "memory_usage": "85MB",
            "status": "PASS"
        }
    ]
}