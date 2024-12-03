require("lib")

local input = GetInput()

local function scanMemory()
    local result = 0
    for _, line in pairs(input) do
        for a, b in string.gmatch(line, "mul%((%d+),(%d+)%)") do
            result = result + (a * b)
        end
    end
    return result
end

print("What do you get if you add up all of the results of the multiplications?\nAnswer: " .. scanMemory())