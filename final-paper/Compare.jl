using Primes
using Plots
using GSL
using Base.Threads
using LaTeXStrings

# functions for Li(x)
sf_li(x) = sf_expint_Ei(log(x))
sf_Li(x::T) where T = sf_li(x) - sf_li(T(2))

N = floor(Int, 1.66e5)
START = 100

prime_count = zeros(N - START + 1)
li_count = zeros(N - START + 1)
pmt_count = zeros(N - START + 1)

# actual primes
@spawn begin
    if isprime(START)
        prime_count[1] = 1
    end
    for i in START+1:N
        if isprime(i)
            prime_count[i - START + 1] = prime_count[i - START] + 1
        else
            prime_count[i - START + 1] = prime_count[i - START]
        end
    end
end

# prime number theorem
@spawn begin
    @threads for i in START:N
        pmt_count[i - START + 1] = i / log(i)
    end
end

# Li(x)
@spawn begin
    @threads for i in START:N
        li_count[i - START + 1] = sf_Li(i) - sf_Li(2)
    end
end

savefig(plot(START:N, [prime_count li_count pmt_count], label=[L"\pi(x)" L"\mathrm{Li}(x)" L"\frac{x}{\ln(x)}"]), "plot1.pdf")
