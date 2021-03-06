def isBalanced(s):
    openBrackets = ['(','[','{']
    closedBrackets = [')',']','}']
    stack = []
    for i in range(len(s)):
        #print(s[i:][:1] in openBrackets)
        if ((i==0  and s[i:][:1] not in openBrackets)) or (s[-1:] in openBrackets):
            return "NO"
        if (s[i:][:1] in openBrackets):
            stack.append(s[i:][:1])
        else:
            index = closedBrackets.index(s[i:][:1])  
            if (len(stack)==0 or  stack.pop()!=openBrackets[index]):
                return "NO"
    return "YES"  


a = ["[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]",
"[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}",
"(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]",
"){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]",
"}(]}){",
"((]()(]([({]}({[)){}}[}({[{])(]{()[]}}{)}}]]{({)[}{(",
"{}{({{}})}[][{{}}]{}{}(){{}[]}{}([[][{}]]())",
"(){}[()[][]]{}(())()[[([])][()]{}{}(({}[]()))()[()[{()}]][]]",
"()([]({}[]){}){}{()}[]{}[]()(()([[]]()))()()()[]()(){{}}()({[{}][]}[[{{}({({({})})})}]])",
"[]([{][][)(])}()([}[}(})}])}))]](}{}})[]({{}}))[])(}}[[{]{}]()[(][])}({]{}[[))[[}[}{(]})()){{(]]){][",
"{()({}[[{}]]()(){[{{}{[[{}]{}((({[]}{}()[])))]((()()))}(()[[[]]])((()[[](({([])()}))[]]))}]})}",
"()(){{}}[()()]{}{}",
"{}()([[]])({}){({[][[][[()]]{{}[[]()]}]})}[](())((())[{{}}])",
"{}(((){}){[]{{()()}}()})[]{{()}{(){()(){}}}}{()}({()(()({}{}()((()((([])){[][{()}{}]})))))})",
"][[{)())))}[)}}}}[{){}()]([][]){{{{{[)}]]{([{)()][({}[){]({{",
"{{}(",
"{[{((({}{({({()})()})[]({()[[][][]]}){}}))){}}]}{}{({((){{}[][]{}[][]{}}[{}])(())}[][])}",
"()[[][()[]][]()](([[[(){()[[]](([]))}]]]))",
"()[]({}{})(()){{{}}()()}({[]()}())[](){}(({()}[{}[{({{}}){({}){({})((({()})))}}}]]))",
"}[{){({}({)})]([}{[}}{[(([])[(}){[]])([]]}(]]]]{][",
"[{]{[{(){[}{}(([(]}])(){[[}(]){(})))}}{{)}}{}][({(}))]}({)",
")})[(]{][[())]{[]{{}}[)[)}[]){}](}({](}}}[}{({()]]",
"[[[({[]}({[][[[[][[{(()[][])}()[][]][]{}]]]]}))][(()){}]]]()[{}([]{}){}{{}}]",
"({[]({[]})}())[][{}[{{(({{{([{}])}}}))}}]]",
"([((()))()])[][][]{}()(([]))[]()[]((){}[]){}(){{}[]}[[{[]}]]",
"[[(((({}{[]{}()}){}{{}}){({[]{[{}]{(){}(((){()}))}()}}[[]]()()[()])[[{}{}]()]}))]]{}[]{}({({{}})})",
"(]{()}((",
"[][(())[({{{()[]}}{[[][[][[[]{{{[()]{{{{}{[]}[][]}}}}}}]]]]}})]]",
"}[})})}[)]{}{)",
"({(}{})))}(}[)[}{)}}[)[{][{(}{{}]({}{[(})[{[({{[}{(]]})}",
']}})[]))]{][])[}(])]({[]}[]([)',
"[{{}{[{{[}[[}([]",
"[([]){}][({})({[(([])[][])][[{}{([{{}{(()){{{({}{{}}())}}[]}}()[()[{{{([](()){[[[]]]})}}}]]}])}]]})]",
"]{}{(}))}](})[{]]()(]([}]([}][}{]{[])}{{{]([][()){{})[{({{{[}{}](]}}",
"{[{}}){(}[][)(}[}][)({[[{]}[(()[}}){}{)([)]}(()))]{)(}}}][",
"(]{}{(}}}[)[",
"[]{}{[[]]}([{}]{}[]){{(())}}",
"[)([{(][(){)[)}{)]]}}([((][[}}(]{}]]}]][(({{{))[[){}{]][))[]{]][)[{{}{()]){)])))){{{[(]}[}}{}]",
"{({(){[[[][]{}[[([]{})]{}]][[]()()]]}})}[{}{{}}]",
")}][(})){))[{}[}",
"{[]{({]}[}}[{([([)([){{}{(}}[]}}[[{[}[[()(])[}[]",
"()()()[]",
"((){}])][]][}{]{)]]}][{]}[)(])[}[({(",
")[((])(]]]]((]){{{{())]}]}(}{([}(({}]])[[{){[}]{{}})[){(",
"}][[{[((}{[]){}}[[[)({[)}]]}(]]{[)[]}{}(){}}][{()]))})]][(((}}",
"([]){}{{}{}}()([([{}{[[]()([(([]()))()[[]]])]}])])",
"[()[[]{{[]}()([])}[]][][]][]()[]{}{}[][]{}{}[()(){}]",
"{[{){]({(((({](]{([])([{{([])[}(){(]](]{[{[]}}())[){})}))[{})))[",
"{}[()[]][]{}{}[[{{[[({})]()[[()]]]}}]]",
"{[{}[][]]}[((()))][]({})[]{}{()}",
"(){[{({})}]}",
"([]])][{)]({)[]))}]())[}]))][}{(}}})){]}]{[)}(][})[[",
"((({{}(([{}(())]))[()]{[[[]()]]}})))",
"}()))}(}]]{{})}][{](]][{]{[[]]]}]]}([)({([))[[(]}])}[}(([{)[)]]([[](]}]}{]{{})[]){]}{])(",
"{}{}{}{[[()]][]}",
")]}]({{})[[[{]{{{}}][))]{{",
"))){({}])}])}}]{)()(}(]}([",
"([[]][])[[]()][]()(([[]]{[()[]{[][{}]}[()]]{}{[]}}{{}()}(()[([][]{})[[{}][]]{}[]])))",
"(]{[({}[){)))}]{[{}][({[({[]))}[}]}{()(([]{]()}})}[]{[)](((]]])([]}}]){)(([]]}[[}[",
"([[]])({}(([(){{}[{}]}]){[{}]}))[][{}{}](){}",
"[][][][][][([])][]{({()}[[()()]{([(){[]{}}{(())}{[](){}()({}())}[({}[[]()])][]])}])}",
"}[{{(}})}}(((())()({]{([]((][(({)[({[]]}[])}]{][{{}]{)][}(])}}}))}}}",
"[]({})()[]{}{}[]({}{})[]{([])()[()][{()({})[{}{[[()]{}[]][]}(({{[]{()()()}{}[]()}[]}){{}{}})]}]}",
"{{(([{)]{}({][{](){({([[[][)}[)})(",
"[{}]{[()({[{}]})]}",
"[[{}]]",
"]{{({[{]}[[)]]}{}))}{){({]]}{]([)({{[]){)]{}){){}()})(]]{{])(])[]}][[()()}",
"{[([}[[{{(]]][}()())]{){(){)]]){})}]{][][(}[]())[}[)})})[][{[)[})()][]))}[[}",
"]()])}[}}}{]]{)[}(}]]])])}{(}{([{]({)]}])(})[{}[)]])]}[]{{)){}{()}]}((}}{({])[}])[]}",
"(]}[{}{{][}))){{{([)([[])([]{[",
"{(()[]){}}(){[]}({{}(()())})([]){}{}(())()[()]{}()",
"{{}[{}[{}[]]]}{}({{[]}})[[(){}][]]{}(([]{[][]()()}{{{()()}{[]}({}[]{()})}{()}[[]][()]}))",
"{[][]}[{}[](){}]{{}{[][{}]}}",
"()(){}(){((){}[])([[]]())}",
"{}[[{[((}[(}[[]{{]([(}]][[",
"{}[([{[{{}()}]{}}([[{}[]]({}{{()}[][][]})])])]",
"{[](}([)(])[]]})()]){[({]}{{{)({}(][{{[}}(]{",
"[][]{{}[](())}{}({[()]}())[][[][({}([{}]))]]",
"((()))[]{[(()({[()({[]}{})]}))]}{[]}{{({}{})[{}{}]{()([()])[{()}()[[]{}()]{}{}[]()]}[[]{[]}([])]}}"]

for i in a:
    print(isBalanced(i))
