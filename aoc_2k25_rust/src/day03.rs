use std::error::Error;
use super::solver::DaySolver;

/// Main function to solve Day 3, Part 1 & 2.
/// This is where the actual logic for Day 3 will go.
pub fn solve(input: &str) -> Result<(i32, i32), Box<dyn Error>> {
    // Placeholder logic for Day 3
    let part1_result = input.len() as i32; // Example: length of the input string
    let part2_result = part1_result * 2; // Example: double the part1 result

    Ok((part1_result, part2_result))
}

// Define the concrete struct for Day 03
pub struct Day03Solver;

// Implement the DaySolver trait for Day03Solver
impl DaySolver for Day03Solver {
    fn solve(&self, input: &str) -> String {
        // Call the specific solve function for Day 2 and format its output
        match solve(input) {
            Ok((part1, part2)) => format!("Part 1: {}\nPart 2: {}", part1, part2),
            Err(e) => format!("Error: {}", e),
        }
    }
}
