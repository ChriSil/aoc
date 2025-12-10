use std::error::Error;
use super::solver::DaySolver;

/// Main function to solve Day 1, Part 1 & 2.
/* pub fn solves(input: &str) -> Result<(i32, i32), Box<dyn Error>> {
 // Models the dial's position (0-99) using modular arithmetic (modulo 100) to simulate circular movement. For all rotations (R and L), the position is calculated using the algebraic formula:
//              (current_a±D)%100+100)(mod100)
// This reliably forces negative remainders (from L rotations) to wrap to a positive index, ensuring correct circular boundary traversal.
    let mut current_a: i32 = 50; // Start Position of Dial
    let mut dial_pos: Vec<i32> = Vec::new();
    let mut cross_counter: i32 = 0;
    dial_pos.push(current_a);

    for line in input.lines() {
        if line.is_empty() {
            continue;
        }
        let (op, num_str) = line.split_at(1);
        let signed_distance: i32 = if let Ok(num) = num_str.parse::<i32>() { // Parse as i32 directly
            match op {
                "L" =>-num,
                "R" =>num,
                _ => continue, // Ignore malformed lines
            }
        }  else{continue;};

        let theoretical_pos:i32 = current_a+signed_distance;        
        // --- Part 2 Calculation ---
        // P2: Calculate how many times 0 (or a multiple of 100) was crossed.
        // The number of crossings is the difference between the number of 100-multiples passed.
        
        let start_boundary: i32;
        let end_boundary: i32;
        // Use Rust's inherent division/floor behavior for positive/negative numbers.
        if signed_distance >= 0 { // Right rotation
            // Rounds down to the nearest lower multiple of 100.
            start_boundary = current_a.div_floor(100);
            end_boundary = theoretical_pos.div_floor(100);
            cross_counter += end_boundary - start_boundary;
        } else { // Left rotation
            // Rounds down to the nearest lower multiple of 100.
            start_boundary = current_a.div_floor(100);
            end_boundary = theoretical_pos.div_floor(100);
            // Must use the absolute difference or ensure the order is E - S to get a positive count.
            cross_counter += (start_boundary - end_boundary).abs(); 
        }

/* // P2, count full rotations, then check if there is a positive or a negative wrap (i.e. crossing 0)
        let full_rota: i32 = signed_distance.abs() / 100;
        cross_counter += full_rota;

        if signed_distance >= 0 { // Right Rotation, check for positive wrap
            cross_counter += if signed_distance.rem_euclid(100) + current_a > 99 { 1 } else { 0 }; 
        }
        else { // Left Rotation, check for negative wrap
            // NOTE: signed_distance % 100 is negative here. We must subtract its absolute value.
            // Use the absolute value of the remainder to find the distance moved within the final partial cycle.
            cross_counter += if  signed_distance.rem_euclid(100) + current_a < 0 { 1 } else { 0 };
        } */

        
// P1. determine new position of arrow, push it onto the vector        
        current_a = (((theoretical_pos) % 100) + 100) % 100;
        dial_pos.push(current_a);


    }
    let target_value = 0;
    let target_count: i32 = dial_pos.iter().filter(|&x| *x ==target_value).count().try_into().unwrap();
    let part1_result = target_count;
    let part2_result = cross_counter+target_count;


    Ok((part1_result, part2_result))
} */


pub fn solve(input: &str) -> Result<(i32, i32), Box<dyn Error>> {
    // Start Position of Dial
    let mut current_a: i32 = 50;
    
    // Part 1: Count times the dial stops at 0 at the end of a rotation
    let mut part1_target_count: i32 = 0;
    
    // Part 2: Count times the dial clicks onto 0 (including during rotations)
    let mut part2_cross_counter: i32 = 0;

    for line in input.lines() {
        if line.is_empty() {
            continue;
        }
        
        // Parse the instruction (e.g., "L68" -> ('L', "68"))
        let (op, num_str) = line.split_at(1);
        
        let signed_distance: i32 = if let Ok(num) = num_str.parse::<i32>() {
            match op {
                "L" => -num,
                "R" => num,
                _ => continue, // Ignore malformed lines
            }
        } else {
            continue;
        };

        // The theoretical, unbounded position after the move
        let theoretical_pos: i32 = current_a + signed_distance;

        // --- Part 2 Calculation: Count cross-overs ---
        
        // Calculate the number of times 0 (or a multiple of 100) was crossed
        // by comparing the start and end values using stable floor division.
        
        // Stable floor division for X / 100
        let floor_div_100 = |x: i32| -> i32 {
            x / 100 - (x < 0 && x % 100 != 0) as i32
        };

        let start_boundary = floor_div_100(current_a);
        let end_boundary = floor_div_100(theoretical_pos);
        
        // The number of times 0 is clicked ONTO during the movement (excluding the final position)
        // is the absolute difference in the 100-multiple boundaries crossed.
        part2_cross_counter += (end_boundary - start_boundary).abs(); 
        
        // NOTE: The total number of times 0 is clicked ONTO is the sum of the Part 1 count
        // and the clicks *during* the rotation. We combine them by using the calculation
        // above, which effectively counts the total number of 100-multiples passed.

        // --- Part 1 Calculation: Final Position ---
        
        // P1. Determine new position of arrow using stable modular arithmetic:
        // (X % N + N) % N ensures a non-negative result.
        current_a = (((theoretical_pos) % 100) + 100) % 100;
        
        // Check if the dial stopped exactly at 0
        if current_a == 0 {
            part1_target_count += 1;
        }
    }
    
    // The Part 2 total is the sum of all times a 100-multiple was crossed.
    // If the movement ends on 0, it is already counted in part2_cross_counter
    // because the final boundary change accounts for it.
    let part2_result = part2_cross_counter;

    Ok((part1_target_count, part2_result))
}







pub struct Day01Solver;

impl DaySolver for Day01Solver {
    fn solve(&self, input: &str) -> String {
        match solve(input) {
            Ok((part1, part2)) => format!("Part 1: {}\nPart 2: {}", part1, part2),
            Err(e) => format!("Error: {}", e),
        }
    }
}
