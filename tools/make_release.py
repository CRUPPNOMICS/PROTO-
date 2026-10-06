# Build DIMPlugin.lua + PROTO_vX_RELEASE.rbxmx + hashes, staged for the PC.  usage: python3 tools/make_release.py 2.35 R235-m2x8-c4
import sys, subprocess, hashlib, shutil, os
ver, salt = sys.argv[1], sys.argv[2]
subprocess.run(['python3', '/home/claude/tools/build_installer.py'], check=True)
src = open('/home/claude/DIMPlugin.lua', encoding='utf-8').read()
assert ']]>' not in src and f'v{ver}' in src.split('\n')[0]
rel = f'/home/claude/PROTO_v{ver}_RELEASE.rbxmx'
open(rel, 'w', encoding='utf-8').write('''<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<Item class="Script" referent="RBX0">
		<Properties>
			<string name="Name">PROTO</string>
			<token name="RunContext">0</token>
			<bool name="Disabled">false</bool>
			<ProtectedString name="Source"><![CDATA[''' + src + ''']]></ProtectedString>
		</Properties>
	</Item>
</roblox>
''')
h = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()
out = '/mnt/user-data/outputs'; os.makedirs(out, exist_ok=True)
shutil.copy('/home/claude/37_dim_plugin_src.lua', out + '/proto_src.lua')
shutil.copy('/home/claude/DIMPlugin.lua', out + '/DIMPlugin.lua')
shutil.copy(rel, out)
row = f"| PROTO_v{ver}_RELEASE.rbxmx | build {ver} | {h(rel)} | salt {salt} |\n"
open('/home/claude/release_hashes_rows.md', 'a').write(row)
print(row)
