<template>
  <div class="hello">
    <h1>選手名鑑</h1>
    <div class="inputData">
      <p>背番号：</p><input type="text" v-model="no">
    </div>
    <div class="inputData">
      <p>名前：</p><input v-model="name">
    </div>
    <div class="inputData">
      <p>チーム：</p>
      <select v-model="team">
        <option value="">Empty</option>
        <option v-for="option in teamList" v-bind:key="option" v-bind:value="option">
          {{ option }}
        </option>
      </select>
    </div>
    <div class="inputData">
      <p>年度：</p>
      <select v-model="info_year">
        <option v-for="year in yearList" v-bind:key="year" v-bind:value="year">
          {{ year }}
        </option>
      </select>
    </div>
    <div class="inputData">
      <button @click="searchPlayer">検索</button>
      <button @click="clearData">クリア</button>
    </div>
    <div>
    <vue-good-table
      class="player-table"
      :columns="columns"
      :rows="playerDataList">
      <template slot="table-row" slot-scope="props">
        <span v-if="props.column.field == 'name' && props.row.position == '投手'">
          <router-link :to="{ path: '/pitching-stats/' + info_year + '/' + props.row.id }">{{props.row.name}}</router-link>
        </span>
        <span v-else-if="props.column.field == 'name' && props.row.position != '投手'">
          <router-link :to="{ path: '/batting-stats/' + info_year + '/' + props.row.id }">{{props.row.name}}</router-link>
        </span>
        <span v-else>
          {{props.formattedRow[props.column.field]}}
        </span>
      </template>
    </vue-good-table>
    </div>
  </div>
</template>

<script>
import BaseballClient from '../services/api';
export default {
  name: 'SearchPlayer',
  data() {
    return {
      playerData: null,
      playerDataList: [],
      playerId: 0,
      teamList: ['C', 'YS', 'G', 'YB', 'D', 'T', 'L', 'H', 'F', 'B', 'M', 'E'],
      yearList: ['2020', '2019', '2018', '2017', '2016', '2015'],
      no: '',
      name: '',
      team: '',
      info_year: '2020',
      columns: [
        {
          label: '背番号',
          field: 'no',
        },
        {
          label: '名前',
          field: 'name',
        },
        {
          label: 'チーム',
          field: 'team',
        },
        {
          label: 'ポジション',
          field: 'position',
        },
      ],
    }
  },
  methods: {
    async searchPlayer() {
      const response = await BaseballClient.getFilteredPlayerData({
        no: this.no,
        name: this.name,
        team: this.team,
        info_year: this.info_year
      });
      this.playerDataList = response;
    },
    clearData() {
      this.no = '';
      this.name = '';
      this.team = '';
      this.playerDataList = [];
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.inputData {
  display: flex;
  align-items: center;
  justify-content: center;
}
button {
  margin: .5em;
}
.player-table {
  width: 50%;
  margin: 0 auto;
}
</style>
