open System

if fsi.CommandLineArgs.Length = 2 then
    let sidesRaw = fsi.CommandLineArgs.[1]
    let parsed, sides = Int32.TryParse sidesRaw
    
    if parsed then
        match sides with
        | 4 | 6 | 12 ->
            let rng = Random()
            let result = (rng.Next() % sides) + 1
            
            printfn "You rolled a %d with a %d sided die." result sides
        | _ -> printfn "The number of sides should be 4, 6 or 12!"
    else printfn "You need to give me an integer!"
else printfn "How many sides?"
