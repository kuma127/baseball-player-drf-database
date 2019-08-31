import Vue from 'vue';
import VueRouter from 'vue-router';
import SearchPlayer from '@/components/SearchPlayer';
import BattingStats from '@/pages/BattingStats';
import PitchingStats from '@/pages/PitchingStats';

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: SearchPlayer },
        { path: '/batting-stats/:playerId', component: BattingStats },
        { path: '/pitching-stats/:playerId', component: PitchingStats },
        { path: '*', redirect: '/'},
    ]
})

export default router