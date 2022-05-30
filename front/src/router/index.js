import { createRouter, createWebHistory } from "vue-router";
import MountainsPage from "@/pages/mountains/MountainsPage.vue";
import MountainsDetailPage from "@/pages/mountainsDetail/MountainsDetailPage.vue";
import HomePage from "@/pages/home/HomePage.vue";
import MountainsAddPage from "@/pages/mountainsAdd/MountainsAddPage.vue";

const routes = [
  {
    path: "/mountains",
    name: "MountainsPage",
    component: MountainsPage,
  },

  {
    path: "/mountains/:id",
    name: "MountainsDetailPage",
    component: MountainsDetailPage,
  },
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },

  {
    path: "/mountains/add",
    name: "MountainsAddPage",
    component: MountainsAddPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
