<template>
  <div class="hello">
    <h1>成績</h1>
    <vue-good-table
      :columns="columns"
      :rows="rows">
    </vue-good-table>
    <router-link :to="{ path: '/' }">戻る</router-link>
  </div>
</template>

<script>
import BaseballClient from '../services/api';
export default {
  name: 'BattingStats',
  data() {
    return {
      playerStats: null,
      columns: [
        {
          label: '選手名',
          field: 'prop',
        },
        {
          label: '',
          field: 'value',
        },
      ],
      rows: [
        {
          prop: '打率',
          value: ''
        },
        {
          prop: '本塁打',
          value: ''
        },
        {
          prop: '打点',
          value: ''
        },
      ]
    }
  },
  methods: {
    async getStats() {
      const DataList = await BaseballClient.getFilteredBattingStats({
        playerId: this.$route.params.playerId,
        year: 2018,
      });
      this.playerStats = DataList[0];
      this.columns[1].label = DataList[0].player.name;
      this.rows[0].value = DataList[0].avg;
      this.rows[1].value = DataList[0].homeRuns;
      this.rows[2].value = DataList[0].runsBattedIn;
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
