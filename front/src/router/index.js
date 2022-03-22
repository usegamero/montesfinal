import { createRouter, createWebHistory } from "vue-router";
import MountainsPage from "@/pages/mountains/MountainsPage.vue";
import RiversPage from "@/pages/rivers/RiversPage.vue";
import HomePage from "@/pages/home/HomePage.vue";

const routes = [
  {
    path: "/mountains",
    name: "MountainsPage",
    component: MountainsPage,
  },

  {
    path: "/rivers",
    name: "RiversPage",
    component: RiversPage,
  },
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
