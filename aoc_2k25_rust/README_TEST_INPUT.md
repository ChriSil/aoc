# Automatic Test Input Scraping for AOC

This project now supports automatic scraping of test inputs from the Advent of Code problem pages!

## How It Works

The system automatically:
1. Fetches the problem page from adventofcode.com
2. Extracts the first example input (typically found in `<pre><code>` blocks)
3. Caches it locally in `input/` directory as `{year}day_{day}_test.txt`
4. Reuses the cached version on subsequent runs

## Usage

### Step 1: Toggle Test Input Mode

In `src/main.rs`, simply change the `use_test_input` flag:

```rust
let use_test_input: bool = true;  // Set to true to use test input
```

### Step 2: Run Your Solution

```bash
cargo run
```

The system will:
- Automatically scrape the test input from the problem page (if not cached)
- Run your solution against the test input
- Display the results

### Step 3: Switch Back to Real Input

When ready to run against the full input:

```rust
let use_test_input: bool = false;  // Set to false to use real input
```

## Example Workflow

1. **Start a new day**
   ```rust
   // In main.rs
   let day_to_run: usize = 5;
   let use_test_input: bool = true;
   ```

2. **Run with test input**
   ```bash
   cargo run
   ```
   
   Output:
   ```
   Fetching test input for Day 5 from AoC problem page...
   Test input saved to aoc_2k25_rust/input/2025day_05_test.txt.
   
   --- Raw Input Preview (Day 5) ---
   3   4
   4   3
   2   5
   [... 3 more lines]
   ---------------------------------
   
   --- Day 5 Solution ---
   Part 1: 11
   Part 2: 31
   ----------------------------
   ```

3. **Verify against expected output** from the problem statement

4. **Switch to real input**
   ```rust
   let use_test_input: bool = false;
   ```

5. **Run and submit**
   ```bash
   cargo run
   ```

## File Locations

Test inputs are cached in:
```
aoc_2k25_rust/input/
├── 2025day_01.txt       # Real input for day 1
├── 2025day_01_test.txt  # Test input for day 1 (scraped)
├── 2025day_02.txt       # Real input for day 2
├── 2025day_02_test.txt  # Test input for day 2 (scraped)
└── ...
```

## Requirements

- Your AOC session cookie must be set in `.env`:
  ```bash
  AOC_SESSION_COOKIE=your_session_cookie_here
  ```

- Dependencies (already added to `Cargo.toml`):
  - `scraper = "0.22"` - For HTML parsing
  - `reqwest` - For HTTP requests
  - `dotenv` - For environment variables

## How the Scraping Works

The `get_test_input()` function in `src/util/input.rs`:

1. Checks for cached test input first
2. If not found, fetches the problem page from `https://adventofcode.com/{year}/day/{day}`
3. Uses CSS selector `article pre code` to find code blocks
4. Extracts the first code block (typically the first example)
5. Saves it locally for reuse

## Tips

- **Manual override**: If the scraped test input isn't correct, you can manually edit the cached test file
- **Multiple examples**: The scraper gets the first example. If you need a different one, edit the cached file
- **Clear cache**: Delete test files in `input/` to force re-scraping

## Troubleshooting

**Problem: No test input found**
- Some problems may not have code blocks in the expected format
- Manually create the test file: `input/{year}day_{day}_test.txt`

**Problem: Wrong test input scraped**
- The scraper picks the first `<pre><code>` block
- Edit the cached file manually with the correct test input

**Problem: Session cookie expired**
- Update your `.env` file with a fresh session cookie from adventofcode.com

## Advanced: Selecting Different Code Blocks

If you need to scrape a different code block (not the first one), modify `src/util/input.rs`:

```rust
// Get the second code block instead
let test_input = document
    .select(&code_selector)
    .nth(1)  // Change from next() to nth(1) for second block
    .ok_or("No test input found in problem page")?
    .text()
    .collect::<String>();
```

## Backward Compatibility

The `test_input()` method in the `DaySolver` trait still exists for manual overrides:

```rust
impl DaySolver for Day01Solver {
    fn solve(&self, input: &str) -> String {
        // Your solution
    }
    
    // Optional: Override with custom test input
    fn test_input(&self) -> Option<&str> {
        Some("custom test input here")
    }
}
```

However, this is now optional - the scraper will handle it automatically!
