# k8sh
Interactive shell wrapper to kubectl.
`k8sh` allows you to save key strokes and see your context and namespace in the command line. Avoid mistakes and save time

# Usage

```
# k8sh
kubectl --context=staging >set_context prod
prod
kubectl --context=prod >set_namespace test
test
kubectl --context=prod --namespace=test > get pods
```

`k8sh` offers:
* constant reminder of your conext and namespace (if set)
* tab completion of all normal kubectl methods
    * currently only `get` and `describe` will auto complete kubernetes objects
* normal command line options and arguments are passed transparently

# Requirements

'k8sh' requires:
*`kubectl` binary must be installed and available on the $PATH
* python 2.7
* a valid kubeconfg at `~/.kube/config` or path set in the environment variable `$KUBECONFIG` 


# Known issues
1: Limited support for the flexible plurality that `kubectl` offers i.e pod vs pods. `k8sh` will still pass the plural version through to `kubectl` but it will not tab complete for existing kubernetes objects

