const githubUser = "anfrann25";
const githubRepo = "hackthebasics.gr";

window.$docsify = {
    name: 'HackTheBasics@docs',
    basePath: `https://raw.githubusercontent.com/${githubUser}/${githubRepo}/main/`,
    loadSidebar: true,
    auto2top: true,
    autoHeader: false,
    search: 'auto',
    breadcrumb: { show: true }
}