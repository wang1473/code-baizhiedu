<template>
  <div class="cart_item" v-show="is_show">
    <div class="cart_column column_1">
      <el-checkbox class="my_el_checkbox" v-model="course.selected"></el-checkbox>
    </div>
    <div class="cart_column column_2">
      <img :src="course.course_img" alt="">
      <span><router-link :to="'/detail/'+course.id">{{ course.name }}</router-link></span>
    </div>
    <div class="cart_column column_3">
      <el-select v-model="expire" size="mini" placeholder="请选择购买有效期" class="my_el_select">
        <el-option label="1个月有效" value="30" key="30"></el-option>
        <el-option label="2个月有效" value="60" key="60"></el-option>
        <el-option label="3个月有效" value="90" key="90"></el-option>
        <el-option label="永久有效" value="10000" key="10000"></el-option>
      </el-select>
    </div>
    <div class="cart_column column_4">¥{{ course.price }}</div>
    <div class="cart_column column_4">
      <el-button type="danger" @click="del_course" icon="el-icon-delete" circle></el-button>
    </div>
  </div>
</template>
<script>
export default {
  name: "CartItem",
  props: ['course'],
  watch: {
    'course.selected': function () {
      // 后台发起请求改变状态
      this.change_select();
    },
    'expire': function () {
      this.change_expire()
    }
  },
  data() {
    return {
      expire: `${this.course.expire_id}`,
      is_show: true
    }
  },
  methods: {
    change_expire() {
      this.$axios({
        url: this.$settings.HOST + 'cart/option/',
        method: 'put',
        data: {
          course_id: this.course.id,
          expire: this.expire
        },
        headers: {
          "Authorization": "jwt " + localStorage.getItem('token'),
        }
      }).then(res => {
        console.log(res)
      }).catch(error => {
        console.log(error)
      })
    },

    del_course() {
      this.$axios({
        url: this.$settings.HOST + 'cart/option/',
        method: 'delete',
        data: {
          course_id: this.course.id,
          selected: this.course.selected
        },
        headers: {
          "Authorization": "jwt " + localStorage.getItem('token'),
        }
      }).then(res => {
        console.log(76, res.data)
        this.$store.commit("add_cart", res.data.cart_length)
        this.is_show = false
      }).catch(error => {
        console.log(error)
      })
    },

    change_select() {
      this.$axios({
        url: this.$settings.HOST + 'cart/option/',
        method: 'patch',
        data: {
          course_id: this.course.id,
          selected: this.course.selected,
        },
        headers: {
          "Authorization": "jwt " + localStorage.getItem('token'),
        }
      }).then(res => {
        console.log(res.data.message)
      }).catch(error => {
        console.log(error)
      })
    },
  },
  created() {
  }
}
</script>

<style scoped>
.cart_item::after {
  content: "";
  display: block;
  clear: both;
}

.cart_column {
  float: left;
  height: 250px;
}

.cart_item .column_1 {
  width: 88px;
  position: relative;
}

.my_el_checkbox {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  margin: auto;
  width: 16px;
  height: 16px;
}

.cart_item .column_2 {
  padding: 67px 10px;
  width: 520px;
  height: 116px;
}

.cart_item .column_2 img {
  width: 175px;
  height: 115px;
  margin-right: 35px;
  vertical-align: middle;
}

.cart_item .column_3 {
  width: 197px;
  position: relative;
  padding-left: 10px;
}

.my_el_select {
  width: 117px;
  height: 28px;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
}

.cart_item .column_4 {
  padding: 67px 10px;
  height: 116px;
  width: 142px;
  line-height: 116px;
}

</style>
