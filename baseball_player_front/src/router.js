import Vue from 'vue';
import VueRouter from 'vue-router';
import SearchPlayer from '@/components/SearchPlayer';
import PlayerStats from '@/pages/PlayerStats'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: SearchPlayer },
        { path: '/stats/:playerId', component: PlayerStats },
        { path: '*', redirect: '/'},
    ]
})

export default router