class Solution:
    def minimumTimeRequired(self, jobs, k):
        jobs.sort(reverse=True)

        workers = [0] * k
        self.best = sum(jobs)

        def dfs(i):
            # Trigger 1
            if i >= len(jobs):
                self.best = min(self.best, max(workers))
                return

            seen = set()

            for j in range(k):
                # Trigger 2
                if workers[j] in seen:
                    continue

                # Trigger 3
                if workers[j] + jobs[i] >= self.best:
                    continue

                seen.add(workers[j])
                workers[j] += jobs[i]

                dfs(i + 1)

                workers[j] -= jobs[i]

        dfs(0)

        # Trigger 4
        return self.best
