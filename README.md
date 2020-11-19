# Commit Syntax

Follow Conventional Commits guidelines: https://www.conventionalcommits.org/en/v1.0.0/

# Release Strategy

Code committed to insights-client-runner will be maintained as a single `master` branch. All PRs are opened against `master`. In the below example, `master` consists of commits A, B, and C.

```
master:   A - B - C
```
### Master -> Nightly
At release time, the latest commit is tagged `1.0.0`, and `master` is force-pushed to the `nightly` release branch. 
```
master:   A - B - C
                   \
nightly:            C (1.0.0)
```

### Nightly -> Beta
At the next release, the cycle is repeated. The latest commit is tagged with a version, and `master` is force-pushed to `nightly`. In addition, assuming no problems have arisen in customer environments, `nightly` is force-pushed to the `beta` release branch.
```
master:   A - B - C - D - E - F
                   \           \
nightly:            \           F (1.1.0)
                     \
beta:                 C (1.0.0)
```

### Beta -> Stable
Next release, the process is repeated once more. The latest commit is tagged with a version, `master` is force-pushed to `nightly`, and `nightly` force-pushed to `beta`. In addition, assuming no problems have arisen in customer environments, `beta` is force-pushed to the `stable` release branch.
```
master:   A - B - C - D - E - F - G - H
                   \           \       \
nightly:            \           \       H (1.2.0)
                     \           \
beta:                 \           F (1.1.0)
                       \
stable:                 C (1.0.0) 
```

This process is repeated weekly. Beta is promoted to stable, nighly is promoted to beta, and the latest commit to master is tagged and promoted to nightly.

### Emergency Fixes
If we ever had to make an emergency fix to all branches, we commit to master and cherry pick to each release branch, upticking the release. The cherry-picked commits will go away once we force-push master to nightly at the next regular release, but since we already commited the fix to master, that's A-OK.
```
master:   A - B - C - D - E - F - G - H - I
                   \           \       \
nightly:            \           \       H - I' (1.2.1)
                     \           \
beta:                 \           F - I' (1.1.1)
                       \
stable:                 C - I' (1.0.1)
```
It's unlikely we'll have to do anything like this, but it helps to have a contingency plan.
