def maxArea(height):
    maxH = 0

    left = 0
    right = len(height) - 1

    while left < right:
        h = (right - left) * min(height[left], height[right])

        maxH = max(maxH, h)

        if height[left] < height[right]:
            left += 1

        elif height[left] >= height[right]:
            right -= 1

    return maxH
