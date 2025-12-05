use std::error::Error;
use super::solver::DaySolver;

/// Main function to solve Day 1, Part 1 & 2.
pub fn solve(input: &str) -> Result<(i32, i32), Box<dyn Error>> {
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

// P2, count full rotations, then check if there is a positive or a negative wrap (i.e. crossing 0)
        let full_rota: i32 = signed_distance.abs() / 100;
        cross_counter += full_rota;

        if signed_distance >= 0 { // Right Rotation, check for positive wrap
            cross_counter += if signed_distance.rem_euclid(100) + current_a > 99 { 1 } else { 0 }; 
        }
        else { // Left Rotation, check for negative wrap
            // NOTE: signed_distance % 100 is negative here. We must subtract its absolute value.
            // Use the absolute value of the remainder to find the distance moved within the final partial cycle.
            cross_counter += if  signed_distance.rem_euclid(100) + current_a < 0 { 1 } else { 0 };
        }
// P1. determine new position of arrow, push it onto the vector        
        current_a = (((theoretical_pos) % 100) + 100) % 100;
        dial_pos.push(current_a);


    }
    let target_value = 0;
    let target_count: i32 = dial_pos.iter().filter(|&x| *x ==target_value).count().try_into().unwrap();
    let part1_result = target_count;
    let part2_result = cross_counter+target_count;


    Ok((part1_result, part2_result))
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
