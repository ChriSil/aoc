use dotenv::dotenv;
use reqwest::blocking::Client;
use scraper::{Html, Selector};
use std::{env, fs, path::Path, error::Error};

const AOC_YEAR: u32 = 2025; 
const PACKAGE_DIR: &str = "aoc_2k25_rust";

/// Fetches the input for a given day, saving it locally if not found.
pub fn get_input(day: u32) -> Result<String, Box<dyn Error>> {    
    // 1. Define local file path
    let filename = format!("{}day_{:02}.txt", AOC_YEAR,day);
    // let path = Path::new("input").join(&filename);
    let dir = Path::new(PACKAGE_DIR).join("input");
    let path = dir.join(&filename);

    // 2. Check if the file already exists (caching)
    if path.exists() {
        println!("Input for Day {} found locally. Reading from file.", day);
        return fs::read_to_string(path).map_err(Into::into);
    }
    
    // --- File not found: Proceed to API fetch ---

    // 3. Load environment variables and get session cookie
    dotenv().ok();
    let session_cookie = env::var("AOC_SESSION_COOKIE")
        .map_err(|_| "AOC_SESSION_COOKIE not set in .env")?;

    // 4. Construct API URL
    let url = format!(
        "https://adventofcode.com/{}/day/{}/input",
        AOC_YEAR, day
    );

    // 5. Make the authorized HTTP request
    println!("Fetching input for Day {} from AoC API...", day);
    let client = Client::new();
    let response = client
        .get(&url)
        .header(
            "Cookie",
            format!("session={}", session_cookie)
        )
        .send()?
        .error_for_status()?; // Check for 4xx/5xx errors

    // 6. Read the input text
    let input = response.text()?;

    // 7. Save the input to the local file
    fs::write(&path, &input)?;
    println!("Input saved to {}.", path.display());

    Ok(input)
}

/// Fetches the test input for a given day by scraping the problem page.
/// Test inputs are typically found in <pre><code> blocks on the problem page.
pub fn get_test_input(day: u32) -> Result<String, Box<dyn Error>> {
    // 1. Define local cache file path for test input
    let filename = format!("{}day_{:02}_test.txt", AOC_YEAR, day);
    let dir = Path::new(PACKAGE_DIR).join("input");
    let path = dir.join(&filename);

    // 2. Check if the test input is already cached
    if path.exists() {
        println!("Test input for Day {} found locally. Reading from file.", day);
        return fs::read_to_string(path).map_err(Into::into);
    }
    
    // --- File not found: Proceed to scrape from problem page ---

    // 3. Load environment variables and get session cookie
    dotenv().ok();
    let session_cookie = env::var("AOC_SESSION_COOKIE")
        .map_err(|_| "AOC_SESSION_COOKIE not set in .env")?;

    // 4. Construct problem page URL
    let url = format!(
        "https://adventofcode.com/{}/day/{}",
        AOC_YEAR, day
    );

    // 5. Make the authorized HTTP request to get the problem page
    println!("Fetching test input for Day {} from AoC problem page...", day);
    let client = Client::new();
    let response = client
        .get(&url)
        .header(
            "Cookie",
            format!("session={}", session_cookie)
        )
        .send()?
        .error_for_status()?;

    // 6. Parse the HTML to extract test input
    let html_content = response.text()?;
    let document = Html::parse_document(&html_content);
    
    // The test input is typically in <pre><code> blocks within the article
    let code_selector = Selector::parse("article pre code")
        .map_err(|_| "Failed to parse CSS selector")?;
    
    // Get the first code block (usually the first example)
    let test_input = document
        .select(&code_selector)
        .next()
        .ok_or("No test input found in problem page")?
        .text()
        .collect::<String>();

    // 7. Save the test input to the local file for caching
    fs::create_dir_all(&dir)?;
    fs::write(&path, &test_input)?;
    println!("Test input saved to {}.", path.display());

    Ok(test_input)
}
