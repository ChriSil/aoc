// src/main.rs
mod util;
mod day01;
mod day02;
mod day03;
mod solver;

use solver::DaySolver;
use day01::Day01Solver;
use day02::Day02Solver;
use day03::Day03Solver;
// use day02::Day02Solver; // Import the specific solver for Day 02

fn main() {
    let day_to_run: usize = 1;

    // Create a vector of boxed DaySolver trait objects
    let solvers: Vec<Box<dyn DaySolver>> = vec![
        Box::new(Day01Solver),
        Box::new(Day02Solver),
        Box::new(Day03Solver),
        // Add other day solvers here as they are implemented
    ];

    if day_to_run == 0 || day_to_run > solvers.len() {
        eprintln!("Invalid day selected: {}. Please choose a day between 1 and {}.", day_to_run, solvers.len());
        return;
    }

    let selected_solver = &solvers[day_to_run - 1]; // Adjust for 0-based indexing

    let day_to_run_u32: u32 = day_to_run.try_into().expect("Day number out of u32 range");

    match util::input::get_input(day_to_run_u32) {
        Ok(input) => {
            println!("\n--- Raw Input Preview (Day {}) ---", day_to_run);
            for (i, line) in input.lines().enumerate() {
                if i < 3 {
                    println!("{}", line);
                } else if i == 3 {
                    println!("[... {} more lines]", input.lines().count() - 3);
                    break;
                }
            }
            println!("---------------------------------");

            let result = selected_solver.solve(&input);
            println!("\n--- Day {} Solution ---", day_to_run);
            println!("{}", result);
            println!("----------------------------");
        }
        Err(e) => {
            eprintln!("Execution failed for Day {}: {}", day_to_run, e);
        }
    }
}
