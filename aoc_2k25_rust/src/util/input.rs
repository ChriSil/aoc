use dotenv::dotenv;
use reqwest::blocking::Client;
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