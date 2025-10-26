main :: IO ()
main = do
    [n, m] <- map read . words <$> getLine
    mapM_ putStrLn [if i <= m then "OK" else "Too Many Requests" | i <- [1..n]]
