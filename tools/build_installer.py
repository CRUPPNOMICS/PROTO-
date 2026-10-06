# Build the paste-in installer from the readable dev installer (37_dim_plugin_src.lua):
# plugin body compacted (Studio's command bar can't set Source >= 200,000 chars), header line with the DIM_V1 marker kept.
import sys
sys.path.insert(0, '/home/claude/tools')
from compact import compact
s = open('/home/claude/37_dim_plugin_src.lua').read()
a = s.index('s.Source = [=====[') + len('s.Source = [=====[')
b = s.index(']=====]')
body = s[a:b]
header = next(l for l in body.split('\n') if 'DIM_V1' in l)
c = header.strip() + '\n' + compact(body)
if len(c) >= 199000: print("WARNING: compact installer is", len(c), "chars - too big for the command bar (Plugins-folder file only)")
open('/home/claude/37_dim_plugin.lua', 'w').write(s[:a] + '\n' + c + '\n' + s[b:])
open('/home/claude/DIMPlugin.lua', 'w').write(body.lstrip('\n'))
print('plugin body (compact):', len(c), ' standalone DIMPlugin.lua:', len(body))
