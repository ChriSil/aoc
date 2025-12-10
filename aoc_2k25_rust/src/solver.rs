pub trait DaySolver {
    fn solve(&self, input: &str) -> String;
    
    /// Returns the test input for this day's problem (if available).
    /// This is typically the example input from the problem statement.
    #[allow(dead_code)]
    fn test_input(&self) -> Option<&str> {
        None // Default implementation returns None
    }
}
