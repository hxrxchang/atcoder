use proconio::input;

fn main() {
    input! {
        n: i64,
        k: i64,
    }
    const MOD: i64 = 1_000_000_007;

    let result = if n == 1 {
        k
    } else if n == 2 {
        k * (k - 1) % MOD
    } else {
        k * (k - 1) % MOD * mod_pow(k - 2, n - 2, MOD) % MOD
    };

    println!("{}", result);
}

fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
    if modulus == 1 {
        return 0;
    }
    let mut result = 1;
    base %= modulus;
    while exp > 0 {
        if exp % 2 == 1 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exp /= 2;
    }
    result
}
