# Compacts a Luau source: removes comments (lexer-aware: strings untouched), indentation and blank lines.
import sys
def strip_comments(src):
    out=[]; i=0; n=len(src)
    while i<n:
        c=src[i]
        if c in '"\'':
            q=c; j=i+1
            while j<n and src[j]!=q:
                if src[j]=='\\': j+=1
                if src[j]=='\n': break
                j+=1
            out.append(src[i:j+1]); i=j+1; continue
        if c=='`':
            j=i+1
            while j<n and src[j]!='`':
                if src[j]=='\\': j+=1
                j+=1
            out.append(src[i:j+1]); i=j+1; continue
        if c=='[' and i+1<n and src[i+1] in '[=':
            j=i+1; eq=0
            while j<n and src[j]=='=': eq+=1; j+=1
            if j<n and src[j]=='[':
                close=']'+'='*eq+']'; k=src.find(close,j)
                out.append(src[i:k+len(close)]); i=k+len(close); continue
        if src.startswith('--',i):
            j=i+2
            if j<n and src[j]=='[':
                k=j+1; eq=0
                while k<n and src[k]=='=': eq+=1; k+=1
                if k<n and src[k]=='[':
                    close=']'+'='*eq+']'; e=src.find(close,k); i=e+len(close); continue
            e=src.find('\n',i); i=n if e<0 else e; continue
        out.append(c); i+=1
    return ''.join(out)
def compact(src):
    s=strip_comments(src)
    lines=[l.strip() for l in s.split('\n')]
    return '\n'.join(l for l in lines if l)
if __name__=='__main__':
    src=open(sys.argv[1]).read(); c=compact(src); open(sys.argv[2],'w').write(c); print(len(src),'->',len(c))
