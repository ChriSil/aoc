use std::error::Error;
use super::solver::DaySolver;

/// Main function to solve Day 2, Part 1 & 2.
/// This is where the actual logic for Day 2 will go.
pub fn solve(input: &str) -> Result<(i32, i32), Box<dyn Error>> {
    // Placeholder logic for Day 2
    let part1_result = input.len() as i32; // Example: length of the input string
    // Step 1, parse input, comma delimited but in one line 11-22, range start is x before the -, range end is after. parse in for loop. for now print. we are using test anyways
    for line in input.split(',') {
        if line.is_empty() {
            continue;
        }
        let parts: Vec<&str> = line.split('-').collect();
        if parts.len() == 2 {
            let range_start = parts[0];
            let range_end = parts[1];
        // Process range_start and range_end as needed
    }
}





    // Step 2, find numbers where digit split middle makes 2 same numbers. 
        // probably all nrs in a list? not sure yet
        // if so, push first lens onto vetor to see how large ranges are for efficiency

    // Step3 push onto the vector

    //Step 4 outside loop add em all up 




    let part2_result = part1_result * 2; // Example: double the part1 result

    Ok((part1_result, part2_result))
}

// Define the concrete struct for Day 02
pub struct Day02Solver;

// Implement the DaySolver trait for Day02Solver
impl DaySolver for Day02Solver {
    fn solve(&self, input: &str) -> String {
        // Call the specific solve function for Day 2 and format its output
        match solve(input) {
            Ok((part1, part2)) => format!("Part 1: {}\nPart 2: {}", part1, part2),
            Err(e) => format!("Error: {}", e),
        }
    }
}
