var NexT = window.NexT || {};
var CONFIG = {
    root: '/',
    scheme: 'Gemini',
    version: '7.4.0',
    exturl: false,
    sidebar: {"position":"left","display":"hide","offset":12,"onmobile":false},
    copycode: {"enable":true,"show_result":false,"style":"mac"},
    back2top: {"enable":true,"sidebar":false,"scrollpercent":false},
    bookmark: {"enable":false,"color":"#222","save":"auto"},
    fancybox: false,
    mediumzoom: false,
    lazyload: false,
    pangu: false,
    algolia: {
        appID: '',
        apiKey: '',
        indexName: '',
        hits: {"per_page":10},
        labels: {"input_placeholder":"Search for Posts","hits_empty":"We didn't find any results for the search: ${query}","hits_stats":"${hits} results found in ${time} ms"}
        },
    localsearch: {"enable":true,"trigger":"auto","top_n_per_article":10,"unescape":true,"preload":true},
    path: 'search.xml',
    motion: {"enable":true,"async":false,"transition":{"post_block":"fadeIn","post_header":"slideDownIn","post_body":"slideDownIn","coll_header":"slideLeftIn","sidebar":"slideUpIn"}},
    translation: {
        copy_button: 'Copy',
        copy_success: 'Copied',
        copy_failure: 'Copy failed'
    },
    sidebarPadding: 40
};