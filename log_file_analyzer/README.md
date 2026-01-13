# Log File Analyzer - Fluent Python Chapter 2 Learning Project

A comprehensive hands-on project to master Python sequences, array types, and data structures as covered in **Fluent Python, Chapter 2: An Array of Sequences**.

## 🎯 Learning Objectives

This project provides practical experience with:

- **List comprehensions and generator expressions**
- **Tuple unpacking and pattern matching (Python 3.10+)**
- **Sequence slicing operations**
- **Flat sequences (`array.array`) vs container sequences (`list`, `tuple`)**
- **Mutable vs immutable sequence behavior**
- **`collections.deque` for efficient queue operations**
- **Sorting with `key` functions**
- **Augmented assignment (`+=`, `*=`) behavior**
- **Sequence multiplication (`seq * n`) pitfalls**

## 📖 Project Overview

Build a web server log analyzer that processes Apache-style log files, performs statistical analysis, and generates reports. This real-world scenario exercises every concept from Fluent Python Chapter 2.

### Sample Log Format (Apache Combined Log)
```
192.168.1.1 - - [01/Jan/2024:10:15:30 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0"
```

## 🚀 Project Stages

### Stage 1: Data Parsing
**Concepts**: List comprehensions, tuple unpacking, tuples as records

#### Task 1.1: Parse Log Lines into Tuples
Create a function that transforms raw log lines into structured tuples:

```python
def parse_log_line(line: str) -> tuple:
    """
    Parse a log line into a tuple: (ip, timestamp, method, path, status, size)
    
    Practice:
    - Using tuples as records with unnamed fields
    - String manipulation or regex parsing
    - Tuple unpacking in the implementation
    """
    pass
```

#### Task 1.2: Batch Processing with Comprehensions
```python
def load_logs(filename: str, filter_successful=False):
    """
    Load and parse log file entries.
    
    Practice:
    - List comprehension for filtered data
    - Generator expression for memory efficiency
    - Choosing between eager and lazy evaluation
    """
    pass
```

**Key Learning**: When to use list comprehensions vs generator expressions based on memory constraints.

---

### Stage 2: Statistical Analysis
**Concepts**: Flat sequences (`array.array`), container sequences, nested structures

#### Task 2.1: Response Size Analysis with `array.array`
```python
from array import array

def analyze_response_sizes(log_entries) -> dict:
    """
    Store response sizes in array.array for memory efficiency.
    Calculate mean, median, and percentiles.
    
    Practice:
    - Using array.array('L') for unsigned long integers
    - Flat sequences for atomic numeric data
    - Comparing memory usage: array vs list
    """
    pass
```

**Key Learning**: Flat sequences are more compact and faster but limited to atomic data types.

#### Task 2.2: Grouping with Nested Data Structures
```python
def group_by_ip(log_entries) -> dict:
    """
    Group requests by IP address.
    Returns: {ip: [(timestamp, path, status), ...]}
    
    Practice:
    - Container sequences with nested tuples
    - Being careful with mutable objects in nested structures
    - Understanding when immutability matters
    """
    pass
```

**Key Learning**: "Immutable" tuples can change when they contain mutable items.

---

### Stage 3: Time-Series Processing
**Concepts**: `collections.deque`, sequence slicing, efficient queue operations

#### Task 3.1: Sliding Window Analysis with `deque`
```python
from collections import deque

class TrafficMonitor:
    """
    Track requests per minute using a sliding window.
    
    Practice:
    - Using deque for efficient append/pop operations
    - Bounded queues with maxlen
    - Thread-safe queue operations
    """
    def __init__(self, window_minutes=5):
        self.window = deque(maxlen=window_minutes * 60)
    
    def add_request(self, timestamp):
        pass
    
    def get_current_rate(self):
        pass
```

**Key Learning**: `deque` is optimized for FIFO operations, unlike lists which are slow for `pop(0)`.

#### Task 3.2: Time-Based Slicing
```python
def get_time_range(sorted_logs, start_time, end_time):
    """
    Extract requests for specific time ranges using slicing.
    
    Practice:
    - Powerful sequence slicing: seq[start:end:step]
    - Using slice objects for readability
    - Combining bisect module with slicing for efficiency
    """
    pass
```

**Key Learning**: Sequence slicing is more powerful than many realize, especially for range queries.

---

### Stage 4: Pattern Matching (Python 3.10+)
**Concepts**: Destructuring, pattern matching with `match/case`

#### Task 4.1: Request Classification
```python
def classify_request(log_entry):
    """
    Classify requests using pattern matching.
    
    Practice:
    - Pattern matching with match/case
    - Destructuring tuples
    - Guard clauses with if conditions
    """
    match log_entry:
        case (ip, ts, "GET", path, 200, size) if size > 10000:
            return "large_success"
        case (ip, ts, "POST", path, 201, _):
            return "created"
        case (ip, ts, method, path, status, _) if 400 <= status < 500:
            return "client_error"
        case (ip, ts, method, path, status, _) if 500 <= status < 600:
            return "server_error"
        case _:
            return "other"
```

**Key Learning**: Pattern matching provides more powerful unpacking than traditional tuple unpacking.

---

### Stage 5: Advanced Sequence Operations
**Concepts**: Sequence multiplication, augmented assignment, mutable vs immutable behavior

#### Task 5.1: Multidimensional Analysis
```python
def create_hourly_status_matrix():
    """
    Create a 2D structure: 24 hours × 10 status code categories
    
    Practice:
    - Correct way to initialize nested lists
    - Understanding seq * n with mutable items
    
    ❌ WRONG: [[0] * 10] * 24  # All rows are the same list!
    ✅ RIGHT: [[0] * 10 for _ in range(24)]  # Each row is independent
    """
    pass
```

**Key Learning**: `seq * n` creates references, not copies, which is dangerous with mutable items.

#### Task 5.2: Augmented Assignment Behavior
```python
def demonstrate_augmented_assignment():
    """
    Show how += behaves differently for mutable vs immutable sequences.
    
    Practice:
    - tuple += tuple (creates new object)
    - list += list (modifies in place, usually)
    - Checking object identity with id()
    """
    # Example:
    # t = (1, 2)
    # id_before = id(t)
    # t += (3,)
    # id_after = id(t)  # Different ID - new tuple created
    
    # lst = [1, 2]
    # id_before = id(lst)
    # lst += [3]
    # id_after = id(lst)  # Same ID - modified in place
    pass
```

**Key Learning**: `+=` creates new objects for immutable sequences but modifies in place for mutable ones.

---

### Stage 6: Sorting and Ranking
**Concepts**: `sorted()`, `min/max` with `key` parameter, multi-criteria sorting

#### Task 6.1: Endpoint Analysis
```python
def top_endpoints(log_entries, n=10):
    """
    Find most frequently accessed paths, sorted by response time.
    
    Practice:
    - Using sorted() with custom key functions
    - Multi-level sorting
    - Lambda vs named functions for keys
    """
    pass

def suspicious_ips(log_entries):
    """
    Find IPs with most errors using min/max with key.
    
    Practice:
    - min/max with key parameter
    - Creating appropriate key functions
    """
    pass
```

**Key Learning**: The `key` parameter works with `sorted()`, `min()`, `max()`, and is incredibly flexible.

---

### Stage 7: Complete Integration
**Concepts**: All of the above combined

```python
class LogReport:
    """
    Complete log analysis system combining all concepts.
    """
    def __init__(self, log_file):
        # Use generator expression to avoid loading everything
        self.entries = None
        self.size_array = array('L')
        self.recent_requests = deque(maxlen=1000)
        
    def generate_report(self) -> dict:
        """
        Comprehensive analysis combining:
        - Parsing (comprehensions, unpacking)
        - Storage (array.array for sizes)
        - Tracking (deque for recent requests)
        - Slicing (time ranges)
        - Sorting (ranking endpoints)
        - Pattern matching (request classification)
        """
        pass
    
    def stream_analyze(self, log_stream):
        """
        Process logs as they stream in.
        
        Practice:
        - Generator-based processing
        - Bounded memory with deque
        - Real-time analysis
        """
        pass
```

---

## 🎓 Bonus Challenges

### 1. Immutability Test
Create a function that uses `hash()` to verify if a tuple of log entries is truly immutable:

```python
def verify_immutable(t):
    """
    Try to hash a tuple to assert its value is fixed.
    A TypeError means it contains mutable items.
    """
    try:
        hash(t)
        return True
    except TypeError:
        return False
```

### 2. Unpacking Generalizations (PEP 448)
Use `*` unpacking to merge multiple log sources:

```python
# Merge logs from multiple files
combined = [*source1, *source2, *source3]

# Dictionary merging
metadata = {**default_config, **user_config}
```

### 3. Ellipsis Notation
Create a custom `LogArray` class supporting NumPy-style indexing:

```python
class LogArray:
    def __getitem__(self, key):
        # Support logs[..., status_code]
        pass
```

### 4. Memory Comparison
Benchmark memory usage for 1 million entries:

```python
import sys

# Compare:
# - list of integers
# - array.array('L') of integers  
# - deque of integers
# Use sys.getsizeof() and memory_profiler
```

---

## ✅ Success Criteria

You've mastered Fluent Python Chapter 2 when you can:

- ✅ Write list/generator comprehensions fluently for data transformation
- ✅ Unpack tuples and use pattern matching naturally
- ✅ Choose between flat (`array`) and container (`list`) sequences based on use case
- ✅ Understand mutable vs immutable sequence implications
- ✅ Use slicing powerfully for data extraction and manipulation
- ✅ Apply `deque` for queue operations where appropriate
- ✅ Sort with complex key functions confidently
- ✅ Recognize when `seq * n` is safe vs dangerous
- ✅ Explain `+=` behavior differences between sequence types

---

## 📚 Related Concepts from Chapter 2

### Flat vs Container Sequences

**Flat sequences** (compact, fast, limited):
- `str`, `bytes`, `bytearray`, `array.array`
- Store atomic data directly in memory
- More memory efficient for large numeric datasets

**Container sequences** (flexible, can hold any type):
- `list`, `tuple`, `collections.deque`
- Store references to objects
- More versatile but can have higher memory overhead

### Mutable vs Immutable

**Immutable**: `tuple`, `str`, `bytes`
- Cannot be changed after creation
- `+=` creates new object
- Safe to use as dict keys (if contents are also immutable)

**Mutable**: `list`, `bytearray`, `array.array`, `deque`
- Can be modified in place
- `+=` usually modifies existing object
- Cannot be dict keys

---

## 🛠️ Getting Started

1. Create a `logs/` directory with sample log files
2. Implement each stage sequentially
3. Write tests to verify your understanding
4. Compare your implementations with the book's principles

### Sample Test Data Generator

```python
import random
from datetime import datetime, timedelta

def generate_sample_logs(filename, n=1000):
    """Generate sample log file for testing."""
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    paths = ['/api/users', '/api/posts', '/home', '/about']
    statuses = [200, 201, 304, 400, 404, 500]
    
    start_time = datetime.now() - timedelta(days=1)
    
    with open(filename, 'w') as f:
        for i in range(n):
            ip = f"192.168.1.{random.randint(1, 255)}"
            ts = start_time + timedelta(seconds=i)
            method = random.choice(methods)
            path = random.choice(paths)
            status = random.choice(statuses)
            size = random.randint(100, 50000)
            
            log_line = f'{ip} - - [{ts.strftime("%d/%b/%Y:%H:%M:%S +0000")}] '
            log_line += f'"{method} {path} HTTP/1.1" {status} {size}\n'
            f.write(log_line)
```

---

## 💡 Tips

- Start simple: get basic parsing working first
- Use `print()` and `type()` liberally to understand what you're working with
- Compare memory usage: `sys.getsizeof()` is your friend
- Read the error messages: Python's TypeError for unhashable types teaches about mutability
- Benchmark performance differences between approaches

---

## 📖 References

- **Fluent Python, 2nd Edition** by Luciano Ramalho - Chapter 2: An Array of Sequences
- Python Documentation: [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- PEP 448: [Additional Unpacking Generalizations](https://www.python.org/dev/peps/pep-0448/)
- PEP 636: [Structural Pattern Matching](https://www.python.org/dev/peps/pep-0636/)

---

**Happy Learning!** 🐍

Remember: "Mastering the standard library sequence types is a prerequisite for writing concise, effective, and idiomatic Python code."
