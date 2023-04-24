using Primes
using StatsBase
using Distributions
using Plots
using DataStructures
using Base.Threads
using GSL

# functions for Li(x)
sf_li(x) = sf_expint_Ei(log(x))
sf_Li(x::T) where T = sf_li(x) - sf_li(T(2))

# gets the differences between consecutive elements in an array
function GetDiffs(arr)
    return ([arr; 0] - [0; arr])[2:end-1]
end

# model with discrete uniform distribution
function CramerModelV1(low, high)
    ps = Int[]
    for i in low:high
        if rand() < 1/log(i)
            push!(ps, i)
        end
    end
    return ps
end

# model with continuous uniform distribution, using prime number theorem
function CramerModelV2(low, high)
    return sort(rand(Uniform(low, high), round(Int, high/log(high) - low/log(low))))
end

# model with continuous uniform distribution, using Li(x)
function CramerModelV3(low, high)
    return sort(rand(Uniform(low, high), round(Int, sf_Li(high) - sf_Li(low))))
end

N = floor(Int, 1.66e5)
START = 100
TRIALS = 100

actual_primes = primes(N)
less_than_100 = collect(Iterators.takewhile(n -> n < START, actual_primes))
actual_primes = SortedSet{Int}(actual_primes)
biggest_gap = maximum(GetDiffs(less_than_100))
last_prime = less_than_100[end]

model_maxs = zeros(N - START + 1)
actual_maxs = zeros(N - START + 1)
for n in START:N
    # check actual gap
    if n in actual_primes
        if n - last_prime > biggest_gap
            global biggest_gap = n - last_prime
        end
        global last_prime = n
    end

    # check model gap, parallelized trials
    model = zeros(TRIALS)
    @threads for i in 1:TRIALS
        # model[i] = maximum(GetDiffs(CramerModelV1(2, n)))
        # model[i] = maximum(GetDiffs(CramerModelV2(2, n)))
        model[i] = maximum(GetDiffs(CramerModelV3(2, n)))
    end

    # update gaps
    model_maxs[n - START + 1] = ceil(Int, sum(model) / TRIALS)
    actual_maxs[n - START + 1] = biggest_gap

    # print progress
    if n % 100 == 0
        println(n)
    end
end

savefig(plot(100:N, [model_maxs actual_maxs], label=["Model Maxes" "Actual Maxes"]), "plot.pdf")
