use std::collections::HashMap;
use std::iter::zip;

use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = fs::read_to_string("input")?;

    println!("{}", solve1(input.clone()));
    println!("{}", solve2(input.clone()));

    Ok(())
}

fn solve1(input: String) -> u64 {
    let nums: Vec<(i64, i64)> = input
        .split('\n')
        .map(|s| {
            let mut parts = s.split_whitespace().map(|num| num.parse::<i64>().unwrap());
            (parts.next().unwrap(), parts.next().unwrap())
        })
        .collect();

    let mut first_list: Vec<i64> = nums.iter().map(|t| t.0).collect();
    let mut second_list: Vec<i64> = nums.iter().map(|t| t.1).collect();

    first_list.sort();
    second_list.sort();

    return zip(first_list.iter(), second_list.iter())
        .map(|(v1, v2)| (v1 - v2).abs() as u64)
        .sum();
}

fn solve2(input: String) -> u64 {
    let nums: Vec<(u64, u64)> = input
        .split('\n')
        .map(|s| {
            let mut parts = s.split_whitespace().map(|num| num.parse::<u64>().unwrap());
            (parts.next().unwrap(), parts.next().unwrap())
        })
        .collect();

    let first_list = nums.iter().map(|t| t.0);
    let second_list = nums.iter().map(|t| t.1);

    let mut freqs = second_list.fold(HashMap::new(), |mut m: HashMap<u64, u64>, v| {
        *m.entry(v).or_default() += 1;
        m
    });

    return first_list
        .map(|n| n * *freqs.entry(n).or_default())
        .sum::<u64>();
}
