<template>
  <div class="hello" v-if="playerStats">
    <h1>成績！</h1>
    <div class="stats">
      <p>{{ playerStats.player.name }} {{ playerStats.year }}年</p>
      <p>打率： {{ playerStats.avg }}</p>
      <p>本塁打： {{ playerStats.homeRuns }}</p>
      <p>打点：{{ playerStats.runsBattedIn }}</p>
    </div>
  </div>
</template>

<script>
import BaseballClient from '../services/api';
export default {
  name: 'PlayerStats',
  data() {
    return {
      playerStats: null,
    }
  },
  methods: {
    async getStats() {
      const DataList = await BaseballClient.getFilteredPlayerStats({
        playerId: this.$route.params.playerId,
        year: 2018,
      });
      this.playerStats = DataList[0];
    }
  },
  created() {
    this.getStats();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.stats {
  display: grid;
}
</style>
