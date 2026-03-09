module Main where

import System.Environment (getArgs)
import Text.Read (readMaybe)
import Data.List (intercalate, foldl')

-- The model state containing all necessary variables for the forecasting
data State = State {
    population :: Double,
    industrialPercent :: Double,
    agriculturalPercent :: Double,
    waterScarcity :: Double,
    lag1 :: Double,
    lag2 :: Double
} deriving (Show)

-- Base demand function. Calculates raw demand based on current state.
baseDemand :: State -> Double
baseDemand s = 
    let wPop = 0.35
        wInd = 0.25
        wAgr = 0.30
        wScar = 0.10
        
        base = (population s * wPop) + (industrialPercent s * wInd) + (agriculturalPercent s * wAgr) + (waterScarcity s * wScar)
        -- Auto-regressive term using lag values to smooth predictions and reflect time-series nature
        arTerm = (lag1 s * 0.7) + (lag2 s * 0.3)
    in (base * 0.6) + (arTerm * 0.4)

-- Pure function that transitions the current state to the next state for the recursive model
nextState :: State -> State
nextState s = 
    let currentDemand = baseDemand s
        -- Simulated scenario dynamics
        newPop = population s * 1.01 -- 1% growth
        newInd = industrialPercent s * 1.015 -- 1.5% growth in industry
        newAgr = agriculturalPercent s * 0.99 -- slight improvements in agriculture efficiency
        newScarcity = min 1.0 (waterScarcity s + (currentDemand * 0.02)) -- Scarcity compounds slowly as demand rises
    in State newPop newInd newAgr newScarcity currentDemand (lag1 s)

-- Forecasting function using foldl' instead of explicit recursion
forecast :: Int -> State -> [(State, Double)]
forecast n initialState = 
    let step (acc, s) _ = 
            let demand = baseDemand s
                s' = nextState s
            in ((s, demand) : acc, s')
        (reversedHistory, _) = foldl' step ([], initialState) [1..n]
    in reverse reversedHistory

-- Helper to convert state and demand to a JSON string for Python ingestion
stateToJSON :: State -> Double -> String
stateToJSON s demand = 
    "{" ++
    "\"population\": " ++ show (population s) ++ ", " ++
    "\"industrial\": " ++ show (industrialPercent s) ++ ", " ++
    "\"agricultural\": " ++ show (agriculturalPercent s) ++ ", " ++
    "\"scarcity\": " ++ show (waterScarcity s) ++ ", " ++
    "\"demand\": " ++ show demand ++
    "}"

-- Arguments parser
parseArgs :: [String] -> Maybe State
parseArgs [pop, ind, agr, scar, l1, l2] = do
    p <- readMaybe pop
    i <- readMaybe ind
    a <- readMaybe agr
    sc <- readMaybe scar
    l1' <- readMaybe l1
    l2' <- readMaybe l2
    return $ State p i a sc l1' l2'
parseArgs _ = Nothing

main :: IO ()
main = do
    args <- getArgs
    case args of
        (stepsStr : restArgs) -> do
            let nSteps = read stepsStr :: Int
            case parseArgs restArgs of
                Just initialState -> do
                    let predictions = forecast nSteps initialState
                    -- Using foldr to process predictions into JSON strings
                    let jsonList = foldr (\(s, d) acc -> stateToJSON s d : acc) [] predictions
                    putStrLn $ "[" ++ intercalate ", " jsonList ++ "]"
                Nothing -> putStrLn "{\"error\": \"Invalid state arguments.\"}"
        _ -> putStrLn "{\"error\": \"Usage: ForecastEngine <steps> <population> <ind> <agr> <scarcity> <lag1> <lag2>\"}"
