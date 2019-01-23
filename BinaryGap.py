def solution(N):
    binary_form = bin(N)[2:]
    binary_gap = binary_form.split('1')[:-1]
    binary_gap = [len(gap) for gap in binary_gap]
    try:
        return max(binary_gap)
    except ValueError:
        return 0
