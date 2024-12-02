use std::iter::empty;

use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = fs::read_to_string("input")?;

    let reports = parse(input);

    println!("{}", solve1(&reports));
    println!("{}", solve2(&reports));

    Ok(())
}

fn parse(input: String) -> Vec<Vec<u64>> {
    input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<u64>().unwrap())
                .collect()
        })
        .collect()
}

fn solve1(reports: &Vec<Vec<u64>>) -> u64 {
    return reports.iter().filter(|&report| is_safe(report)).count() as u64;
}

fn solve2(reports: &Vec<Vec<u64>>) -> u64 {
    return reports
        .iter()
        .filter(|&report| {
            (0..report.len())
                .map(|i| {
                    let mut spliced = report.clone();
                    spliced.splice(i..i + 1, empty::<u64>());
                    spliced
                })
                .any(|dampened| is_safe(&dampened))
        })
        .count() as u64;
}

fn is_safe(report: &Vec<u64>) -> bool {
    let (mut dec, mut inc, mut maxd) = (true, true, 0);
    for i in 1..report.len() {
        let vii = *report.get(i - 1).unwrap();
        let vi = *report.get(i).unwrap();

        dec = dec && vii < vi;
        inc = inc && vii > vi;
        maxd = maxd.max(vii.abs_diff(vi));
    }
    return (dec || inc) && 1 <= maxd && maxd <= 3;
}
