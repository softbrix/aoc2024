require("lib")

local input = GetInput()
local list = 'do()' .. table.concat(input)

local function findMul(line)
    local result = 0
    for a, b in line:gmatch("mul%((%d+),(%d+)%)") do
        result = result + (a * b)
    end
    return result
end

local function scanMemory()
    local result = 0

    local str = list:split("don't()")
    for _, part in pairs(str) do
        local _, stop = part:find("do%(%)")
        if stop then
            result = result + findMul(part:sub(stop))
        end
    end
    return result
end

print("What do you get if you add up all of the results of just the enabled multiplications?\nAnswer: " .. scanMemory())