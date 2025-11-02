import random
import time
import matplotlib.pyplot as plt
from typing import List, Dict


# -------------------------------
# Selection Algorithm Implementations
# -------------------------------
class SelectionAlgorithms:
    @staticmethod
    def randomized_select(arr: List[int], k: int) -> int:
        """Randomized Quickselect to find the k-th smallest element."""
        arr_copy = arr.copy()

        def partition(left, right, pivot_idx):
            pivot_value = arr_copy[pivot_idx]
            arr_copy[pivot_idx], arr_copy[right] = arr_copy[right], arr_copy[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if arr_copy[i] < pivot_value:
                    arr_copy[i], arr_copy[store_idx] = arr_copy[store_idx], arr_copy[i]
                    store_idx += 1
            arr_copy[store_idx], arr_copy[right] = arr_copy[right], arr_copy[store_idx]
            return store_idx

        def quickselect(left, right, k_smallest):
            if left == right:
                return arr_copy[left]
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)
            if k_smallest == pivot_idx:
                return arr_copy[k_smallest]
            elif k_smallest < pivot_idx:
                return quickselect(left, pivot_idx - 1, k_smallest)
            else:
                return quickselect(pivot_idx + 1, right, k_smallest)

        return quickselect(0, len(arr_copy) - 1, k)

    @staticmethod
    def deterministic_select(arr: List[int], k: int) -> int:
        """Deterministic selection (Median of Medians) to find k-th smallest element."""
        arr_copy = arr.copy()

        def partition_mom(left, right, pivot_idx):
            """Partition around the pivot value at pivot_idx."""
            pivot_value = arr_copy[pivot_idx]
            arr_copy[pivot_idx], arr_copy[right] = arr_copy[right], arr_copy[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if arr_copy[i] < pivot_value:
                    arr_copy[i], arr_copy[store_idx] = arr_copy[store_idx], arr_copy[i]
                    store_idx += 1
            arr_copy[store_idx], arr_copy[right] = arr_copy[right], arr_copy[store_idx]
            return store_idx

        def find_median(left, right):
            """Find median of a small array using sorting."""
            segment = arr_copy[left:right + 1]
            segment.sort()
            median_idx = left + (right - left) // 2
            # Update the array with sorted segment
            for i in range(left, right + 1):
                arr_copy[i] = segment[i - left]
            return median_idx

        def select(left, right, k_smallest):
            if left == right:
                return arr_copy[left]

            # Dividing array into groups of 5 and find medians
            n = right - left + 1
            medians = []

            for i in range(left, right + 1, 5):
                group_right = min(i + 4, right)
                median_idx = find_median(i, group_right)
                medians.append(median_idx)

            # Finding median of medians recursively
            num_medians = len(medians)
            if num_medians == 1:
                mom_idx = medians[0]
            else:
                # Creating a list of median values for recursive call
                median_values = [arr_copy[idx] for idx in medians]
                # Using randomized select to find median of medians (to avoid infinite recursion)
                mom_value = SelectionAlgorithms.randomized_select(median_values, num_medians // 2)
                # Finding the index of mom_value in the original array
                mom_idx = -1
                for i in range(left, right + 1):
                    if arr_copy[i] == mom_value:
                        mom_idx = i
                        break

            # Partition around median of medians
            pivot_idx = partition_mom(left, right, mom_idx)

            # Determining which partition contains k_smallest
            if k_smallest == pivot_idx:
                return arr_copy[k_smallest]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)

        return select(0, len(arr_copy) - 1, k)


# -------------------------------
# Test Case Generator
# -------------------------------
def generate_test_cases() -> Dict[int, Dict[str, List[int]]]:
    """Generate multiple test cases with different distributions and sizes."""
    test_cases = {}
    sizes = [100, 500, 1000, 5000]
    for size in sizes:
        test_cases[size] = {
            'random': [random.randint(1, size * 10) for _ in range(size)],
            'sorted': list(range(1, size + 1)),
            'reverse_sorted': list(range(size, 0, -1)),
            'all_equal': [42] * size,
            'few_unique': [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
        }
    return test_cases


# -------------------------------
# Run Test Cases
# -------------------------------
def run_test_cases():
    """Run all test cases, measure execution time, and calculate ratio."""
    selector = SelectionAlgorithms()
    test_cases = generate_test_cases()
    results = []

    print(f"{'Size':<8} {'Distribution':<15} {'Randomized (s)':<15} {'Deterministic (s)':<18} {'Ratio (Det/Rand)':<15}")
    print("-" * 80)

    # Loop through each size and distribution
    for size, distributions in test_cases.items():
        for dist_name, arr in distributions.items():
            k = size // 2  # pick median

            # Verify the array is not empty
            if len(arr) == 0:
                continue

            # Measure Randomized Select
            start = time.perf_counter()
            try:
                rand_result = selector.randomized_select(arr, k)
                rand_time = time.perf_counter() - start
            except Exception as e:
                print(f"Randomized select failed for size={size}, distribution={dist_name}: {e}")
                continue

            # Measure Deterministic Select
            start = time.perf_counter()
            try:
                det_result = selector.deterministic_select(arr, k)
                det_time = time.perf_counter() - start
            except Exception as e:
                print(f"Deterministic select failed for size={size}, distribution={dist_name}: {e}")
                continue

            # Verify correctness
            expected = sorted(arr)[k]
            if rand_result != expected:
                print(
                    f"Randomized result error for size={size}, distribution={dist_name}: got {rand_result}, expected {expected}")
            if det_result != expected:
                print(
                    f"Deterministic result error for size={size}, distribution={dist_name}: got {det_result}, expected {expected}")

            # Compute ratio
            ratio = det_time / rand_time if rand_time > 0 else float('inf')

            # Store results for plotting
            results.append({
                'size': size,
                'distribution': dist_name,
                'randomized_time': rand_time,
                'deterministic_time': det_time,
                'ratio': ratio
            })

            # Print formatted output
            print(f"{size:<8} {dist_name:<15} {rand_time:<15.6f} {det_time:<18.6f} {ratio:<15.2f}")

    return results


# -------------------------------
# Plot Graph
# -------------------------------
def plot_results(results):
    """Plot execution times for both algorithms."""
    if not results:
        print("No results to plot")
        return

    # Group by distribution type for better visualization
    distributions = set(r['distribution'] for r in results)

    plt.figure(figsize=(12, 8))

    for dist in distributions:
        dist_results = [r for r in results if r['distribution'] == dist]
        sizes = [r['size'] for r in dist_results]
        rand_times = [r['randomized_time'] for r in dist_results]
        det_times = [r['deterministic_time'] for r in dist_results]

        plt.subplot(2, 1, 1)
        plt.plot(sizes, rand_times, 'o-', label=f'Randomized ({dist})')
        plt.subplot(2, 1, 2)
        plt.plot(sizes, det_times, 's--', label=f'Deterministic ({dist})')

    plt.subplot(2, 1, 1)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Randomized Selection Algorithm Performance')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Deterministic Selection Algorithm Performance')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Main method
if __name__ == "__main__":
    print("Running Selection Algorithm Comparison...")
    results = run_test_cases()  # Run test cases
    if results:
        plot_results(results)  # Plot graph
    else:
        print("No results to display")