/* Exit function */
use std::process::exit;
/* Environment variables */
use std::env;
/* File IO */
use std::io::prelude::*;
use std::fs::File;

macro_rules! error {
    ($cond:expr, $msg:expr) => {
        if $cond {
            eprintln!($msg);
            exit(1);
        }
    };
}

fn main() {
    let args: Vec<String> = env::args().collect();
    error!(args.len() < 2, "Syntax:\t./cc6809 fname.c");
    
    let mut cfile: File;
    match File::open(&*args[1]) {
        Ok(file) => cfile = file,
        Err(err) => error!(true, "Failed to open file"),
    }
    //println!("{:?}", cfile);
    //let mut cfile = (File::open(&*args[1]))?;
}
