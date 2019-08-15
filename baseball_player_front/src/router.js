import Vue from 'vue';
import VueRouter from 'vue-router';
import SearchPlayer from '@/components/SearchPlayer';
import BattingStats from '@/pages/BattingStats'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: SearchPlayer },
        { path: '/batting-stats/:playerId', component: BattingStats },
        { path: '*', redirect: '/'},
    ]
})

export default router