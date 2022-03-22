use rand::Rng;

fn main() {
    let max_steps:u32 = 10000000;
    let pi = approx_pi(max_steps);
    println!("Approximation of pi: {}", pi);
}

fn approx_pi(max_steps: u32) -> f64 {
    let mut rng = rand::thread_rng();
    let mut count = 0;
    for _i in 0..max_steps {
        let x:f64 = rng.gen::<f64>();
        let y:f64 = rng.gen::<f64>();
        let r:f64 = x * x + y * y;
        if  r <= 1.0 {
            count += 1;
        }
    }
    let pi:f64 = 4.0 * count as f64 / max_steps as f64;
    return pi
}
