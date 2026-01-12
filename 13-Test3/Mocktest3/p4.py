def f(fnc, res):
    filtered_results = list(filter(fnc, res))
    return max(filtered_results) - min(filtered_results)
