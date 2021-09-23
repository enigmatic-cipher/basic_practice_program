import sys
import textwrap
module = ", ".join(sorted(sys.builtin_module_names))
print(textwrap.fill(module, width=50))
